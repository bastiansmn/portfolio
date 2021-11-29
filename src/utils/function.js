export default function setActive(anchor) {
    document.querySelectorAll(".anchor > a")
        .forEach(e => {
            e.classList.remove("anchor_active");
        });
    document.querySelector(`a[href='#${anchor}']`).classList.add("anchor_active");
}