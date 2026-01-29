/* ==================== BANNER SLIDER JAVASCRIPT ==================== */

document.addEventListener('DOMContentLoaded', function() {
    // ==================== SLIDER CHÍNH (Video Banner) ====================
    const slides = document.querySelectorAll('.banner-slide');
    
    // Kiểm tra nếu không có slide thì bỏ qua
    if (slides.length === 0) {
        return;
    }
    
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const dots = document.querySelectorAll('.dot-btn');
    
    let currentSlide = 0;
    let isTransitioning = false;
    const totalSlides = slides.length;
    const slideDuration = 8000; // 8 giây
    
    // Lấy video của slide hiện tại
    function getCurrentVideo() {
        return slides[currentSlide].querySelector('video');
    }
    
    // Reset và phát video từ đầu
    function playCurrentVideo() {
        const video = getCurrentVideo();
        if (video) {
            video.currentTime = 0;
            video.play().catch(() => {});
        }
    }
    
    // Chuyển đến slide cụ thể với hiệu ứng mượt
    function goToSlide(newIndex) {
        if (isTransitioning || newIndex === currentSlide) return;
        isTransitioning = true;
        
        const currentSlideEl = slides[currentSlide];
        const nextSlideEl = slides[newIndex];
        
        // Thêm hiệu ứng transform cho video
        currentSlideEl.classList.add('transforming');
        nextSlideEl.classList.add('transforming');
        
        // Fade out slide hiện tại
        currentSlideEl.style.opacity = '0';
        
        // Sau 350ms (nửa thời gian transition), hiển thị slide mới
        setTimeout(() => {
            // Cập nhật dots
            dots[currentSlide].classList.remove('bg-white/90', 'active');
            dots[currentSlide].classList.add('bg-white/40');
            dots[newIndex].classList.remove('bg-white/40');
            dots[newIndex].classList.add('bg-white/90', 'active');
            
            // Ẩn slide cũ, hiện slide mới
            currentSlideEl.classList.remove('opacity-100');
            currentSlideEl.classList.add('opacity-0');
            nextSlideEl.classList.remove('opacity-0');
            nextSlideEl.classList.add('opacity-100');
            
            // Reset và phát video mới
            const nextVideo = nextSlideEl.querySelector('video');
            if (nextVideo) {
                nextVideo.currentTime = 0;
                nextVideo.play().catch(() => {});
            }
            
            // Bỏ hiệu ứng transform
            setTimeout(() => {
                currentSlideEl.classList.remove('transforming');
                nextSlideEl.classList.remove('transforming');
                currentSlideEl.style.opacity = '';
                isTransitioning = false;
                currentSlide = newIndex;
                resetAutoSlideTimer();
            }, 350);
        }, 350);
    }
    
    // Chuyển slide tiếp theo
    function nextSlide() {
        const newIndex = (currentSlide + 1) % totalSlides;
        goToSlide(newIndex);
    }
    
    // Chuyển slide trước đó
    function prevSlide() {
        const newIndex = (currentSlide - 1 + totalSlides) % totalSlides;
        goToSlide(newIndex);
    }
    
    // Timer cho auto-slide
    let autoSlideTimer;
    
    function resetAutoSlideTimer() {
        clearInterval(autoSlideTimer);
        if (!isTransitioning) {
            autoSlideTimer = setInterval(nextSlide, slideDuration);
        }
    }
    
    // Event listeners cho buttons
    if (prevBtn) {
        prevBtn.addEventListener('click', function(e) {
            e.preventDefault();
            prevSlide();
        });
    }
    
    if (nextBtn) {
        nextBtn.addEventListener('click', function(e) {
            e.preventDefault();
            nextSlide();
        });
    }
    
    // Event listeners cho dots
    dots.forEach((dot, index) => {
        dot.addEventListener('click', function(e) {
            e.preventDefault();
            if (index !== currentSlide) {
                goToSlide(index);
            }
        });
    });
    
    // Bắt đầu auto-slide
    resetAutoSlideTimer();
    
    // Phát video đầu tiên
    playCurrentVideo();
    
    // ==================== BANNER PHỤ (Auto Slider) ====================
    const autoSliderTrack = document.getElementById('autoSliderTrack');
    
    if (autoSliderTrack) {
        const autoSliderItems = autoSliderTrack.querySelectorAll('.auto-slider-item');
        
        let autoCurrentIndex = 0;
        const autoItemCount = 4; // 4 banners thật
        const autoSlideDuration = 3000; // 3 giây
        
        function autoNextSlide() {
            autoCurrentIndex++;
            
            // Tính transform
            const translateX = -(autoCurrentIndex * 50);
            autoSliderTrack.style.transform = `translateX(${translateX}%)`;
            
            // Khi đến clone cuối cùng (index 4), reset về 0 (không có animation)
            if (autoCurrentIndex >= autoItemCount) {
                setTimeout(() => {
                    autoSliderTrack.style.transition = 'none';
                    autoSliderTrack.style.transform = 'translateX(0)';
                    autoCurrentIndex = 0;
                    
                    // Restore transition sau khi reset
                    setTimeout(() => {
                        autoSliderTrack.style.transition = 'transform 0.5s ease-in-out';
                    }, 50);
                }, 500);
            }
        }
        
        // Bắt đầu auto-slide (chờ 3 giây trước khi chuyển đầu tiên)
        let autoSliderInterval = setInterval(autoNextSlide, autoSlideDuration);
    }
});

