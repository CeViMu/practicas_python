function FizzBuzz (num ){
    let mensaje = "";
    if(num%3===0){
        mensaje+= "Fizz";
    }
        
    if(num%5===0){
        mensaje+= "Buzz";
    }

    console.log(mensaje || "n")
}

FizzBuzz(15);