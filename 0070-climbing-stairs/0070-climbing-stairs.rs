impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        let mut a = 1;
        let mut b = 1;
        for _ in 2..n+1{
            (a, b) = (b, a+b);
        }
        return b;
    }
}