const ALL_COINS: [i32; 8] = [1,2,5,10,20,50,100,200];

fn make_change(amount: i32, coins: &[i32]) -> i32 {  //&[usize]  reference to a arbitrarily sized array of usizes 
    if amount < 0 {
        return 0
    }
    if coins.len() == 0 {
        return 0
    }
    if amount == 0 {
        return 1
    }
    let num_with_amount = make_change(amount - coins[0], coins);
    let num_without_first_coin = make_change(amount, &coins[1..]);

    return num_with_amount + num_without_first_coin;
}


fn main() {
    println!("{}", make_change(200, &ALL_COINS))
}
