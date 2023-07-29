// document.getElementById('clickable').addEventListener('click', clickDiv);
//
// function clickDiv() {
//     document.getElementById('clickable').innerHTML = "{{ url 'home' }}"; // Changes text inside div one time only when clicked
// }

function myFunction() {
  location.replace("{{ url 'pages:home' }}")
}