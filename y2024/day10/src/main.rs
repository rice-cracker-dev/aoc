use std::{collections::HashSet, fs::read_to_string};

fn read_inputs() -> Vec<Vec<usize>> {
    let content = read_to_string("./day10/inputs.txt").unwrap();
    let mut vec: Vec<Vec<usize>> = Vec::new();

    for line in content.lines() {
        vec.push(
            line.trim()
                .chars()
                .map_while(|x| x.to_digit(10))
                .map(|x| x.try_into().unwrap())
                .collect(),
        )
    }

    vec
}

fn traverse_height_map(
    slice: &[Vec<usize>],
    x: usize,
    y: usize,
    ph: Option<usize>,
    reachable: &mut HashSet<(usize, usize)>,
    rating: &mut usize,
) {
    let x_slice = &slice[y];
    let h = x_slice[x];

    if let Some(prev_height) = ph {
        if prev_height + 1 != h {
            return;
        }

        if h == 9 {
            reachable.insert((x, y));
            *rating += 1;
            return;
        }
    }

    if x > 0 {
        traverse_height_map(slice, x - 1, y, Some(h), reachable, rating)
    }
    if x + 1 < x_slice.len() {
        traverse_height_map(slice, x + 1, y, Some(h), reachable, rating)
    }
    if y > 0 {
        traverse_height_map(slice, x, y - 1, Some(h), reachable, rating)
    }
    if y + 1 < slice.len() {
        traverse_height_map(slice, x, y + 1, Some(h), reachable, rating)
    }
}

fn main() {
    let height_map = read_inputs();
    let mut trails = 0;
    let mut trails_ratings = 0;

    for (y, line) in height_map.iter().enumerate() {
        for (x, height) in line.iter().enumerate() {
            if *height == 0 {
                let mut reachable: HashSet<(usize, usize)> = HashSet::new();
                let mut rating = 0;
                traverse_height_map(&height_map, x, y, None, &mut reachable, &mut rating);
                trails += reachable.len();
                trails_ratings += rating;
            }
        }
    }

    println!("part1: {trails}");
    println!("part2: {trails_ratings}");
}
