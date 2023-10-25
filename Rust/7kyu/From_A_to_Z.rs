//Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter. 
//Note that if the range is given in capital letters, return the string in capitals also!

fn gimme_the_letters(sp: &str) -> String {
    let x : Vec<char> = sp.chars().collect();
    let first = x[0];
    let second = x[2];
    let alphabet : String = (first..=second).collect();
    alphabet
}
