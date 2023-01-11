console.log(d3.select('.selectpicker'));

var addresses = d3.select('.selectpicker');

console.log(addresses.node().value);

addresses.on('change', pop_list_price);

function pop_list_price(e) {
  console.log(d3.select('.selectpicker').node().value);

  let addr = d3.select('.selectpicker').node().value;
  console.log(addr);

  // Set the List Price field with data based on the address selected
  // For now, we are setting the value to the address. Once we prove
  // That we can set this field and display it, then we will retrieve
  // the actual data from the csv file to display the price for row
  // with this address instead.
  let lp = document.getElementById('list_price');
  lp.innerHTML = addr;
  list_price.value = address;
}
