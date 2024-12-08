use std::{fs::read_to_string, io::Result};

struct Point(isize, isize);
struct UnsignedPoint(usize, usize);

fn read_inputs() -> Vec<String> {
    let content = read_to_string("./day4/inputs.txt").expect("Can't read inputs.txt");
    let mut vec: Vec<String> = Vec::new();

    for line in content.lines().map(String::from).collect::<Vec<String>>() {
        vec.push(line);
    }

    vec
}

fn to_signed_point(UnsignedPoint(x, y): UnsignedPoint) -> Option<Point> {
    Some(Point(isize::try_from(x).ok()?, isize::try_from(y).ok()?))
}

fn to_unsigned_point(Point(x, y): Point) -> Option<UnsignedPoint> {
    Some(UnsignedPoint(usize::try_from(x).ok()?, usize::try_from(y).ok()?))
}

// casting hell
fn calculate_dir(UnsignedPoint(x, y): UnsignedPoint, Point(dx, dy): &Point) -> Option<UnsignedPoint> {
    let Point(ax, ay) = to_signed_point(UnsignedPoint(x, y))?;
    let UnsignedPoint(ux, uy) = to_unsigned_point(Point(ax + dx, ay + dy))?;

    Some(UnsignedPoint(ux, uy))
}

fn check_dir(grid: &Vec<String>, word: &str, coord: UnsignedPoint, dir: Point) -> bool {
    let Some(line) = grid.get(coord.1) else { return false };
    let Some(char) = line.chars().nth(coord.0) else { return false };

    if word.starts_with(char) && word.chars().count() == 1 {
        return true;
    }

    if !word.starts_with(char) {
        return false;
    } 

    let Some(calculated_coord) = calculate_dir(coord, &dir) else { return false; };

    check_dir(grid, &word[1..], calculated_coord, dir)
}

fn main() -> Result<()> {
    let grid = read_inputs();
    let xmas = "XMAS";
    let mas = "MAS";
    
    let mut xmas_count: usize = 0;
    let mut mas_count: usize = 0;
    for (y, line) in grid.iter().enumerate() {
        for (x, _) in line.chars().enumerate() {
            xmas_count += usize::from(check_dir(&grid, xmas, UnsignedPoint(x, y), Point(-1, -1)));
            xmas_count += usize::from(check_dir(&grid, xmas, UnsignedPoint(x, y), Point(0, -1)));
            xmas_count += usize::from(check_dir(&grid, xmas, UnsignedPoint(x, y), Point(1, -1)));
            xmas_count += usize::from(check_dir(&grid, xmas, UnsignedPoint(x, y), Point(1, 0)));
            xmas_count += usize::from(check_dir(&grid, xmas, UnsignedPoint(x, y), Point(1, 1)));
            xmas_count += usize::from(check_dir(&grid, xmas, UnsignedPoint(x, y), Point(0, 1)));
            xmas_count += usize::from(check_dir(&grid, xmas, UnsignedPoint(x, y), Point(-1, 1)));
            xmas_count += usize::from(check_dir(&grid, xmas, UnsignedPoint(x, y), Point(-1, 0)));

            let Some(tl) = calculate_dir(UnsignedPoint(x, y), &Point(-1, -1)) else { continue };
            let Some(tr) = calculate_dir(UnsignedPoint(x, y), &Point(1, -1)) else { continue };
            let Some(br) = calculate_dir(UnsignedPoint(x, y), &Point(1, 1)) else { continue };
            let Some(bl) = calculate_dir(UnsignedPoint(x, y), &Point(-1, 1)) else { continue };
            let tl_br = check_dir(&grid, mas, tl, Point(1, 1));
            let br_tl = check_dir(&grid, mas, br, Point(-1, -1));
            let tr_bl = check_dir(&grid, mas, tr, Point(-1, 1));
            let bl_tr = check_dir(&grid, mas, bl, Point(1, -1));

            if (tr_bl || bl_tr) && (tl_br || br_tl) { 
                mas_count += 1
            }
        }
    }

    println!("part1: {xmas_count}");
    println!("part2: {mas_count}");

    Ok(())
}
