document.addEventListener('DOMContentLoaded', function () {
    const searchBar = document.querySelector('.search-bar');

    if (searchBar) {
        searchBar.addEventListener('keypress', function (e) {
            if (e.key === 'Enter' && e.target.value.trim() !== '') {
                alert('Recherche: ' + e.target.value.trim());
                e.target.value = ''; // Clear search bar after submission
            }
        });
    }
});
