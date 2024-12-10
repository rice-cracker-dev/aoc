use std::fs::read_to_string;

fn read_inputs() -> Vec<Option<usize>> {
    let content = read_to_string("./day9/inputs.txt").unwrap();
    let mut vec: Vec<Option<usize>> = Vec::new();

    let mut id = 0;
    for (i, char) in content.trim().chars().enumerate() {
        let size = char.to_digit(10).unwrap();
        if i % 2 == 0 {
            (0..size).for_each(|_| vec.push(Some(id)));
            id += 1;
        } else {
            (0..size).for_each(|_| vec.push(None));
        }
    }

    vec
}

fn reallocate_block(slice: &[Option<usize>]) -> Vec<Option<usize>> {
    let mut vec = slice.to_vec();
    let vec_len = vec.len();
    let mut start = 0;
    let mut end = vec_len - 1;

    while start < end {
        if vec.get(end).unwrap().is_none() {
            end -= 1;
            continue;
        };

        if vec.get(start).unwrap().is_some() {
            start += 1;
            continue;
        }

        vec.swap(start, end);
    }

    vec.to_vec()
}

fn get_right_file_block(slice: &[Option<usize>], offset: usize) -> Option<(usize, usize, usize)> {
    let mut id: Option<usize> = None;
    let mut size = 0;

    for (i, allocation) in slice.iter().rev().enumerate().skip(offset) {
        let Some(alloc_id) = allocation else {
            if size > 0 {
                return Some((id.unwrap(), slice.len() - i, size));
            }

            continue;
        };

        if id.is_none_or(|a| a == *alloc_id) {
            size += 1;
            id = Some(*alloc_id);

            continue
        }

        return Some((id.unwrap(), slice.len() - i, size));
    }

    None
}

fn get_left_free_block(slice: &[Option<usize>], offset: usize) -> Option<(usize, usize)> {
    let mut size = 0;

    for (i, allocation) in slice.iter().enumerate().skip(offset) {
        if allocation.is_some() {
            if size > 0 {
                return Some((i - size, size));
            }

            size = 0;
            continue;
        }

        size += 1
    }

    None
}

fn swap_blocks(slice: &mut [Option<usize>], a: usize, b: usize, size: usize) {
    (0..size).for_each(|i| slice.swap(a + i, b + i));
}

fn reallocate_file(slice: &[Option<usize>]) -> Vec<Option<usize>> {
    let mut vec = slice.to_vec();
    let mut file_offset = 0;

    while let Some((_, file_pos, file_size)) = get_right_file_block(&vec, file_offset) {
        let mut free_offset = 0;
        while let Some((free_pos, free_size)) = get_left_free_block(&vec, free_offset) {
            if free_pos > file_pos {
                break;
            }

            if free_size >= file_size {
                swap_blocks(&mut vec, free_pos, file_pos, file_size);
                break;
            }

            free_offset = free_pos + free_size;
        }

        file_offset = vec.len() - file_pos;
    }

    vec
}

fn calculate_checksum(slice: &[Option<usize>]) -> usize {
    slice.iter().enumerate().filter(|(_, v)| v.is_some()).map(|(i, v)| i * v.unwrap()).sum()
}

fn main() -> std::io::Result<()> {
    let vec = read_inputs();
    let recb = reallocate_block(&vec);
    let recf = reallocate_file(&vec);

    println!("part1: {}", calculate_checksum(&recb));
    println!("part2: {}", calculate_checksum(&recf));

    Ok(())
}
