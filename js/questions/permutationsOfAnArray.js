function permute(array) {
    let result = []
    function exec(index, visited, temp) {
        if (temp.length == array.length) {
            result.push([...temp])
            return
        }
        for (let i = 0; i < array.length; i++) {
            if (!visited[i]) {
                visited[i] = true
                temp.push(array[i])
                exec(index + 1, visited, temp)
                visited[i] = false
                temp.pop()
            }
        }
    }
    exec(0, new Array(array.length).fill(false), [])
    console.log(result)
}


permute([1, 2, 3])