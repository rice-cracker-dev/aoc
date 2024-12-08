use std::{cmp::Ordering, fs, iter::Peekable};

#[derive(PartialEq, Eq)]
enum Order {
    Ascending,
    Descending,
}

fn read_input() -> Vec<Vec<usize>> {
    let mut grid: Vec<Vec<usize>> = Vec::new();
    let lines: Vec<String> = fs::read_to_string("./day2/inputs.txt")
        .expect("Can't read inputs.txt")
        .lines()
        .map(String::from)
        .collect();

    for line in &lines {
        grid.push(
            line.split(" ")
                .map(|str| str.parse::<usize>().unwrap())
                .collect(),
        );
    }

    grid
}

fn is_safe(mut iter: Peekable<std::slice::Iter<'_, usize>>) -> bool {
    let mut order: Option<Order> = None;

    while let Some(num) = iter.next() {
        let Some(next) = iter.peek() else {
            return true
        };

        match num.cmp(next) {
            Ordering::Less => {
                if order.is_some() && order != Some(Order::Ascending) {
                    break;
                }

                order = Some(Order::Ascending);
            }

            Ordering::Greater => {
                if order.is_some() && order != Some(Order::Descending) {
                    break;
                }

                order = Some(Order::Descending);
            }

            Ordering::Equal => {
                break;
            }
        }

        if num.abs_diff(**next) > 3 {
            break
        }
    }

    false
}

fn main() -> std::io::Result<()> {
    let grid = read_input();
    let mut p1_answer: usize = 0;
    let mut p2_answer: usize = 0;

    for data in grid {
        if is_safe(data.iter().peekable()) {
            p1_answer += 1;
        }

        // brute-force goes BRRRRR
        for (i, _) in data.iter().enumerate() {
            let mut cloned = data.clone();
            cloned.remove(i);
            if is_safe(cloned.iter().peekable()) {
                p2_answer += 1;
                break;
            }
        }
    }

    println!("part1: {}", p1_answer);
    println!("part2: {}", p2_answer);

    Ok(())
}
