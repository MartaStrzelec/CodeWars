//Turn an area of a square in to an area of a circle that fits perfectly inside the square.

pub const PI: f64 = 3.14159265358979323846264338327950288f64;

fn square_area_to_circle(size:f64) -> f64 {
    PI * size / 4.0
}
