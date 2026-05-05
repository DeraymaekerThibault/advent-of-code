fn main() {
    let input = include_str!("../input.txt");
    println!("Part 1: {}", part1(input)); // i64 implements Display, so {} works
    println!("Part 2: {}", part2(input));
}

fn part1(input: &str) -> i64 {
    let mut pos: i64 = 50;
    let mut count = 0;

    for line in input.lines() {
        // Split the first character (direction) from the rest (number)
        let (dir, amount_str) = line.split_at(1);
        let amount: i64 = amount_str.parse().unwrap();

        let offset: i64 = if dir == "R" { amount } else { -amount };
        // rem_euclid always returns a non-negative remainder, unlike % in Rust
        pos = (pos + offset).rem_euclid(100);

        if pos == 0 {
            count += 1;
        }
    }

    count
}

fn part2(input: &str) -> i64 {
    let mut pos: i64 = 50;
    let mut count = 0;

    for line in input.lines() {
        let (dir, amount_str) = line.split_at(1);
        let amount: i64 = amount_str.parse().unwrap();

        let step: i64 = if dir == "R" { 1 } else { -1 };

        for _ in 0..amount {
            pos = (pos + step).rem_euclid(100);
            if pos == 0 {
                count += 1;
            }
        }
    }

    count
}
