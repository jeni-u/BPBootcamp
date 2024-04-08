function pizzaOven(crustType, sauceType, cheeses, toppings){
    var pizza = {};
    pizza.crustType = crustType;
    pizza.sauceType = sauceType;
    pizza.cheeses = cheeses;
    pizza.toppings = toppings;
    
    return pizza;
}

var p1 = pizzaOven("deep dish", "traditional",["mozzarella"] , ["pepperoni", "sausages"])
console.log(p1) 

/*function randomPizza(){
    
    var crustType = ["deep dish", "hand tossed"]
    var cheeses = ["mozzarella", "feta"]
    var sauceType = ["marinara", "traditional"]
    var toppings = ["pepperoni", "sausages"]

    function randomElement(arr) {
        return arr[Math.floor(Math.random() * arr.length)];
    }
    var pizza = {
        crustType : randomElement(crustType),
        cheeses : randomElement(cheeses),
        sauceType : randomElement(sauceType),
        toppings : randomElement(toppings)
    }
    return pizza;
}
var p1 = randomPizza();
console.log("Crust:", p1.crustType);
console.log("Sauce:", p1.sauceType);
console.log("Cheese:", p1.cheeses);
console.log("Toppings:", p1.toppings);*/