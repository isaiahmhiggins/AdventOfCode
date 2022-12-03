use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    if let Ok(lines) = read_lines("./input") {
        let mut max_cals: u64 = 0;
        let mut current_cals: u64 = 0;
        for line in lines {
            if let Ok(cals) = line {
                if cals == "" {
                    if current_cals > max_cals {
                        max_cals = current_cals;
                    }
                    current_cals = 0;
                } else {
                    let i: Result<u64, std::num::ParseIntError> = cals.trim().parse();
                    if let Ok(i) = i {
                        current_cals += i;
                    } else {
                        println!("Could not parse: {cals}");
                    }
                }
            }
        }
        println!("Max cals: {max_cals}");
    }
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
