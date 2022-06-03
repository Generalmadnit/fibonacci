import React from 'react'

const fibonacci(n) {
    
	let prev = 0, curr = 1, sum, output = [prev, curr];
	
    for (i = 2; i < n; i++) {
        sum = prev + curr;
        prev = curr;
        curr = sum;
        output.push(sum);
    }
    return output;
}
console.log(fibonacci(8));

module.exports = { fibonacci };

export default fibonacci