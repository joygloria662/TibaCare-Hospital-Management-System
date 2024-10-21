import React, {useState, useEffect} from "react";

function Gallery({ images }){
    const [imageIndex, setImageIndex] = useState(0)

    useEffect(()=>{
        const interval = setInterval(()=>{
                setImageIndex(prevIndex => (prevIndex + 1)%images.length)
            }, 5000);
        return ()=>clearInterval(interval);
    }, [images.length])
    
    return (
        <div className="gallery">
            {images.length>0 && (
                <div className="galleryItem">
                    <img
                        src={images[imageIndex].url}
                        alt={images[imageIndex].alt}
                        className="galleryImage"
                    />
                </div>
            )}
        </div>
    )
}

export default Gallery;