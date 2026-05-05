fn main() {
    let input = include_str!("../input.txt");
    println!("Part 1: {}", part1(input));
    println!("Part 2: {}", part2(input));
}

// Parse the input into an iterator of (start, end) pairs.
// We return `impl Iterator` — a Rust way of saying "some iterator type, I won't tell you which".
// The `'_` lifetime means the iterator borrows from `input` and can't outlive it.
fn parse_ranges(input: &str) -> impl Iterator<Item = (u64, u64)> + '_ {
    input.trim().split(',').map(|range| {
        // Closures in Rust look like |args| body — similar to Python lambdas but multi-line
        let (a, b) = range.split_once('-').unwrap();
        (a.parse().unwrap(), b.parse().unwrap())
    })
}

fn sum_matching(input: &str, predicate: impl Fn(u64) -> bool) -> u64 {
    // Functions can take other functions/closures as arguments via `impl Fn(T) -> U`
    parse_ranges(input)
        .flat_map(|(start, end)| start..=end) // flatten each range into individual numbers
        .filter(|&n| predicate(n)) // keep only numbers matching the predicate
        .sum() // sum is a consuming iterator adapter
}

fn is_divisible_by_repdigit(n: u64) -> bool {
    let s = n.to_string();
    let len = s.len();
    if len % 2 != 0 {
        return false;
    }
    let k = len / 2;
    // u64::pow(base, exp) — integer exponentiation
    let divisor = 10u64.pow(k as u32) + 1;
    n % divisor == 0
}

fn has_repeated_sequence(n: u64) -> bool {
    let s = n.to_string();
    if s.len() <= 1 {
        return false;
    }
    // Double the string and check if it appears in the middle
    // e.g. "1212" -> "12121212", strip first and last char -> "212121"
    // "1212" appears in "212121" iff the sequence repeats
    let doubled = s.repeat(2);
    let inner = &doubled[1..doubled.len() - 1];
    inner.contains(s.as_str())
}

fn part1(input: &str) -> u64 {
    sum_matching(input, is_divisible_by_repdigit)
}

fn part2(input: &str) -> u64 {
    sum_matching(input, has_repeated_sequence)
}
