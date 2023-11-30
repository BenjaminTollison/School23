use std::io;
fn main() {
    println!("Guess an integer");
    println!("hope you ain't a screw up");
    println!("this is a life or death situation");

    let mut guess = String::new();
    io::stdin().read_line(&mut guess).expect("Failed to read line");
    
    println!("You guessed: {guess}");
}
