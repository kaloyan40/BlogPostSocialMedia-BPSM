const container = document.querySelector('.responsive-gallery-main .container');
const posts = Array.from(document.querySelectorAll('.responsive-gallery-main .post'));

function generateMasonryGrid(columns) {
    while (container.firstChild) {
        container.removeChild(container.firstChild);
    }

    const columnWrappers = [];
    for (let i = 0; i < columns; i++) {
        const columnDiv = document.createElement('div');
        columnDiv.classList.add('column');
        container.appendChild(columnDiv);
        columnWrappers.push(columnDiv);
    }

    posts.forEach((post, index) => {
        const column = index % columns;
        columnWrappers[column].appendChild(post);
    });
}

let previousScreenSize = window.innerWidth;

window.addEventListener('resize', () => {
    if (window.innerWidth < 600 && previousScreenSize >= 600) {
        generateMasonryGrid(1);
    } else if (window.innerWidth >= 600 && window.innerWidth < 1000 && (previousScreenSize < 600 || previousScreenSize >= 1000)) {
        generateMasonryGrid(2);
    } else if (window.innerWidth >= 1000 && previousScreenSize < 1000) {
        generateMasonryGrid(4);
    }
    previousScreenSize = window.innerWidth;
});

if (previousScreenSize < 600) {
    generateMasonryGrid(1);
} else if (previousScreenSize >= 600 && previousScreenSize < 1000) {
    generateMasonryGrid(2);
} else {
    generateMasonryGrid(4);
}