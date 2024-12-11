use std::{collections::HashMap, fs::read_to_string};

fn read_inputs() -> HashMap<usize, usize> {
    let content = read_to_string("./day11/inputs.txt").unwrap();
    let mut map: HashMap<usize, usize> = HashMap::new();
    
    for num in content.trim().split(' ').map(|x| x.parse::<usize>().unwrap()) {
        map.insert(num, 1);
    }

    map
}

fn add_count(map: &mut HashMap<usize, usize>, key: usize, count: usize) {
    let key_count = map.get(&key).unwrap_or(&0);
    map.insert(key, key_count + count);
}

fn main() {
    let mut map = read_inputs();

    //println!("{}", blink_count(125, 6, 1, &mut result_map));

    for n in 0..75 {
        let mut new_map: HashMap<usize, usize> = HashMap::new();

        for (key, count) in map.keys().map(|k| map.get_key_value(k).unwrap()) {
            if *key == 0 {
                add_count(&mut new_map, 1, *count);
                continue
            }

            let key_str = key.to_string();
            let key_str_len = key_str.len();

            if key_str_len % 2 == 0 {
                add_count(&mut new_map, key_str[0..key_str_len / 2].parse::<usize>().unwrap(), *count);
                add_count(&mut new_map, key_str[key_str_len / 2..key_str_len].parse::<usize>().unwrap(), *count);
                continue
            }

            add_count(&mut new_map, key * 2024, *count);
        }
        map = new_map;

        if n == 24 || n == 74 {
            println!("{}", map.values().sum::<usize>())
        }
    }

}
