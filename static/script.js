document.addEventListener("DOMContentLoaded", () => {
    const openButtons = document.querySelectorAll(".openBtn");
    const closeButtons = document.querySelectorAll(".closeBtn");

    openButtons.forEach((btn) => {
        btn.addEventListener("click", () => {
            const dialog = btn.nextElementSibling;
            if (dialog) dialog.showModal();
        });
    });

    closeButtons.forEach((btn) => {
        btn.addEventListener("click", () => {
            const dialog = btn.closest("dialog");
            if (dialog) dialog.close();
        });
    });
});