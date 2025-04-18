// const apiUrl = 'https://fakestoreapi.com/products/1';  // Sample API

// fetch(apiUrl)
//   .then(response => response.json())
//   .then(product => {
//     console.log("Product Data:", product);  // See this in console

//     const container = document.getElementById('product-container');

//     const tile = document.createElement('div');
//     tile.className = 'product-tile';

//     tile.innerHTML = `
//       <h2>${product.title}</h2>
//       <p>${product.description}</p>
//       <p><strong>Brand:</strong> ${product.category}</p>
//       <p><strong>Price:</strong> ₹${product.price}</p>
//     `;

//     container.appendChild(tile);
//   })
//   .catch(error => {
//     console.error('Error fetching product:', error);
//   });
const apiUrl = 'http://127.0.0.1:8000/products/';  // Your Django API

fetch(apiUrl)
  .then(response => response.json())
  .then(products => {
    console.log("Product Data:", products);  // Log the products array

    const container = document.getElementById('product-container');
    container.innerHTML = '';  // Clear the container before appending new products

    // Loop through the products array and create a tile for each product
    products.forEach(product => {
      const tile = document.createElement('div');
      tile.className = 'product-tile';

      tile.innerHTML = `
        <h2>${product.name}</h2>
        <p>${product.description}</p>
        <p><strong>Brand:</strong> ${product.brand}</p>
        <p><strong>Price:</strong> ₹${product.price}</p>
      `;

      container.appendChild(tile);
    });
  })
  .catch(error => {
    console.error('Error fetching product:', error);
  });
