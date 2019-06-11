// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
// The sum of these multiples is 23.
// Find the sum of all the multiples of 3 or 5 below 1000.

fn main() {
    //let seq = 3..1001;
    //println!(type(seq));  -- // How should I be printing type of var? SO suggestion is call an invalid method and read compiler error [typename] has no method......
    let mut sum_ = 0;
    for n in 3..1000{ // "for n in 3..=999" (w/o "=" it excludes endpoint) would also give same range
        if (n % 5 == 0) || (n % 3 == 0) {
            sum_ = sum_ + n;  
        }
    }
    println!("{}", sum_)
}
