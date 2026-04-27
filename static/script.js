document.addEventListener("DOMContentLoaded", () => {
    const openButtons = document.querySelectorAll(".openBtn");
    const closeButtons = document.querySelectorAll(".closeBtn");

    openButtons.forEach((btn) => {
        btn.addEventListener("click", () => {
            const targetId = btn.dataset.target;
            const dialog = document.getElementById(targetId);
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