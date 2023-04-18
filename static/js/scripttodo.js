let items = [];

function addItem() {
  const input = document.getElementById("input");
  const list = document.getElementById("list");
  const item = input.value;
  if (item !== "") {
    items.push(item);
    const li = document.createElement("li");
    li.appendChild(document.createTextNode(item));
    li.onclick = () => {
      li.classList.toggle("finished");
    };
    list.appendChild(li);
    input.value = "";
  }
}
