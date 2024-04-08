function reverse(arr) {
    // your code here
    for(var i=0;i<arr.length;i++){
        arr.reverse()
    }
    return arr;
}

var result = reverse(["a", "b", "c", "d", "e"]);
console.log(result); // we expect back ["e", "d", "c", "b", "a"]
