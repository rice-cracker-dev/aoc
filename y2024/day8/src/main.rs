use std::{collections::{HashMap, HashSet}, fs::read_to_string};

use itertools::Itertools;

fn read_inputs() -> (isize, HashMap<char, Vec<(isize, isize)>>) {
    let mut map: HashMap<char, Vec<(isize, isize)>> = HashMap::new();
    let content = read_to_string("./inputs.txt").unwrap();

    for (y, line) in content.lines().enumerate() {
        for (x, char) in line.chars().enumerate() {
            if char == '.' {
                continue;
            }

            match map.get_mut(&char) {
                None => { 
                    map.insert(char, vec![(x.try_into().unwrap(), y.try_into().unwrap())]);
                }
                Some(entries) => {
                    entries.push((x.try_into().unwrap(), y.try_into().unwrap()));
                }
            }
        }
    }

    (content.lines().count().try_into().unwrap(), map)
}

fn out_of_bound(size: isize, (x, y): (isize, isize)) -> bool {
    let bound = 0..size;
    !bound.contains(&x) || !bound.contains(&y)
}

fn add_pair((x1, y1): (isize, isize), (x2, y2): (isize, isize)) -> (isize, isize) {
    (x1 + x2, y1 + y2)
}

fn sub_pair((x1, y1): (isize, isize), (x2, y2): (isize, isize)) -> (isize, isize) {
    (x1 - x2, y1 - y2)
}

fn part1(bound: isize, map: HashMap<char, Vec<(isize, isize)>>) {
    let mut antinode_set: HashSet<(isize, isize)> = HashSet::new();

    for k in map.keys() {
        for pair in map.get(k).unwrap().iter().combinations(2) {
            let (pair1, pair2) = (pair[0], pair[1]);
            let d = sub_pair(*pair2, *pair1);
            let a1 = sub_pair(*pair1, d);
            let a2 = add_pair(*pair2, d);

            if !out_of_bound(bound, a1) {
                antinode_set.insert(a1);
            }

            if !out_of_bound(bound, a2) {
                antinode_set.insert(a2);
            }
        }
    

    println!("part1: {}", antinode_set.len());
}

fn part2(bound: isize, map: HashMap<char, Vec<(isize, isize)>>) {
    let mut antinode_set: HashSet<(isize, isize)> = HashSet::new();

    for k in map.keys() {
        for pair in map.get(k).unwrap().iter().combinations(2) {
            let (pair1, pair2) = (pair[0], pair[1]);
            let d = sub_pair(*pair2, *pair1);
            let mut a1 = sub_pair(*pair1, d);
            let mut a2 = add_pair(*pair2, d);

            antinode_set.insert(*pair1);
            antinode_set.insert(*pair2);

            while !out_of_bound(bound, a1) {
                antinode_set.insert(a1);
                a1 = sub_pair(a1, d);
            }

            while !out_of_bound(bound, a2) {
                antinode_set.insert(a2);
                a2 = add_pair(a2, d);
            }
        }
    }

    println!("part2: {}", antinode_set.len());
}

fn main() -> std::io::Result<()> {
    let (bound, map) = read_inputs();
    part1(bound, map.clone());
    part2(bound, map.clone());
    Ok(())
}
