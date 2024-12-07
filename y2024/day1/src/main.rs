use std::fs;

fn read_input() -> (Vec<i32>, Vec<i32>) {
    let mut left = Vec::new();
    let mut right = Vec::new();

    let lines: Vec<String> = fs::read_to_string("./inputs.txt")
        .expect("Can't read inputs.txt")
        .lines()
        .map(String::from)
        .collect();

    for line in &lines {
        let mut split = line.split("   ");
        left.push(split.next().unwrap().parse::<i32>().unwrap());
        right.push(split.next().unwrap().parse::<i32>().unwrap());
    }

    left.sort();
    right.sort();

    (left, right)
}

fn main() -> std::io::Result<()> {
    let (lefts, rights) = read_input();
    let mut total = 0;
    let mut total_similarity: usize = 0;

    for (left, right) in lefts.iter().zip(rights.iter()) {
        let diff = left - right;
        let abs_diff = diff.abs();

        total += abs_diff;
        total_similarity += (*left as usize) * rights.iter().filter(|&x| x == left).count();
    }

    println!("part1: {}", total);
    println!("part2: {}", total_similarity);

    Ok(())
}
