var f = [0, 1];
function myFib(num) {
    if (num > 1) {
        f.push(f[f.length - 1] + f[f.length - 2]);
        myFib(num - 1);
    } else if (num == 1 || num == 0) {
        return f[num];
    } else if (num < 0) {
        return;
    }
    return f;
}

function fib(n) {
    if (n == 0 || n == 1) {
        return n;
    }
    return fib(n - 1) + fib(n - 2);
}

const seq = 30;

console.log("\n");
console.time("fib");
console.log(fib(seq));
console.timeEnd("fib");

console.log("\n");
console.time("myFib");
res = myFib(seq);
console.log(res[res.length-1]);
console.timeEnd("myFib");
console.log("\n");
