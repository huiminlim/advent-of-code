use std::env;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::PathBuf;

fn main() {
    // Load the puzzle input
    let mut path = env::current_dir().unwrap();
    path.push(PathBuf::from("data\\data.txt"));
    println!("Loading puzzle input from: {:?}", path);

    let mut input: Vec<Vec<i32>> = Vec::new();
    let file = File::open(path);
    match file {
        Ok(file) => {
            for line in io::BufReader::new(file).lines() {
                match line {
                    Ok(line) => {
                        let v: Vec<i32> = line
                            .split_terminator("")
                            .skip(1)
                            .map(|x| x.parse::<i32>().unwrap())
                            .collect();
                        input.push(v);
                    }
                    Err(_) => println!("Parse line error"),
                }
            }
        }
        Err(_) => println!("Error"),
    }

    // Puzzle 1
    // Compute the gamma rate
    // Get the first bit of each number in row
    let ncol = input[0].len();
    let mut gamma = 0;
    let mut episilon = 0;
    for i in 0..ncol {
        let mut count_1 = 0;
        let mut count_0 = 0;
        for number in &input {
            match number[i] {
                1 => count_1 += 1,
                0 => count_0 += 1,
                _ => {}
            }
        }

        // Derive gamma
        if count_1 > count_0 {
            gamma = gamma << 1 | 1;
        } else {
            gamma = gamma << 1;
        }

        // Derive episilon
        if count_1 > count_0 {
            episilon = episilon << 1;
        } else {
            episilon = episilon << 1 | 1;
        }
    }

    println!("Gamma: {:?}", gamma);
    println!("Episilon: {:?}", episilon);
    println!("Power: {:?}", gamma * episilon);
}
