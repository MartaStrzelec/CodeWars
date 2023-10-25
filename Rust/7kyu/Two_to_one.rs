//Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

fn longest(a1: &str, a2: &str) -> String {
    let mut x : Vec<char> = [a1, a2].join("").chars().collect();
    x.sort();
    x.dedup();
    x.iter().collect()
}
