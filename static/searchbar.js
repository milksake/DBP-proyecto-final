function search(url) {
    const searchBarInput = document.querySelector('.searchbar input');
    window.location.href = url + searchBarInput.value;
}