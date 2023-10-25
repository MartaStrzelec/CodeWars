//Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. 
//You can guarantee that input is non-negative.

fn count_bits(n: i64) -> u32 {
  n.count_ones()
}
