class PowerSet {

    constructor(){
        this.result = []
    }
    
    solve(s, index, temp){
        if(index >= s.length){
            this.result.push(temp)
            return;
        }
        this.solve(s, index+1, [...temp, s[index]])
        this.solve(s, index+1,[...temp]);
    }

    AllPossibleStrings(s){
        //code here
        this.solve(s,0,[]);
        console.log(this.result)
    }
}

new PowerSet().AllPossibleStrings('abc')