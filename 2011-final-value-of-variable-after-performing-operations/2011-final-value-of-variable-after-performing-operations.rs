use std::collections::HashMap;
impl Solution {
    pub fn final_value_after_operations(operations: Vec<String>) -> i32 {
        let mut mapping: HashMap<&str, i8> = HashMap::new();
        mapping.insert("++X", 1);
        mapping.insert("X++", 1);
        mapping.insert("--X", -1);
        mapping.insert("X--", -1);
        let mut result: i32 = 0;

        for op in &operations {
            let value = mapping.get(op.as_str()).expect("Operation not in map");
            result += *value as i32;
        }
        result
    }
}
