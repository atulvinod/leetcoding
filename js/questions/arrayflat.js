// here the 'this' will refer to the array itself  
  Array.prototype.flat = function(array = this){
      for(let k = 0 ; k < array.length ; k++){
          if(Array.isArray(array[k])){
            let z = this.flat(array[k])
            array.splice(k,1,...z)
          }
      }
      return array
  }
  
  let k = [1,2,3,[4,5,[6]],7,8]
  k.flat()
  console.log(k)