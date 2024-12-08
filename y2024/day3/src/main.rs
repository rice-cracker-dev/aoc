use std::fs::read_to_string;

use regex::Regex;

fn read_inputs() -> String {
    read_to_string("./inputs.txt").expect("Can't read inputs.txt.")
}

fn main() {
    let mul_regex = Regex::new(r"^mul\(([0-9]*,[0-9]*)\)").unwrap();
    let do_regex = Regex::new(r"^do\(\)").unwrap();
    let dont_regex = Regex::new(r"^don't\(\)").unwrap();
    let content = read_inputs();

    let length = content.chars().count();
    let mut i: usize = 0;
    let mut can_do = true;
    let mut p1_answer = 0;
    let mut p2_answer = 0;
    while i < length {
        let sliced = &content[i..length];

        if do_regex.is_match(sliced) {
            can_do = true;
            i += 4;
            continue;
        }

        if dont_regex.is_match(sliced) {
            can_do = false;
            i += 7;
            continue;
        }

        let Some(captured) = mul_regex.captures(sliced) else {
            i += 1;
            continue;
        };

        let group: Vec<usize> = captured
            .get(1)
            .unwrap()
            .as_str()
            .split(",")
            .map(|x| x.parse::<usize>().unwrap())
            .collect();

        p1_answer += group[0] * group[1];
        if can_do {
            p2_answer += group[0] * group[1];
        }

        i += captured.get(0).unwrap().as_str().chars().count();
    }

    println!("part1: {}", p1_answer);
    println!("part2: {}", p2_answer);
}
