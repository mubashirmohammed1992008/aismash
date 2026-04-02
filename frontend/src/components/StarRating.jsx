import React from 'react';
import { Star, StarHalf } from 'lucide-react';

export default function StarRating({ rating }) {
  const fullStars = Math.floor(rating);
  const tempVal = rating - fullStars;
  const hasHalfStar = tempVal >= 0.25 && tempVal <= 0.75;
  const addsOne = tempVal > 0.75 ? 1 : 0;
  
  const totalFull = fullStars + addsOne;
  const emptyStars = 5 - totalFull - (hasHalfStar ? 1 : 0);

  return (
    <div className="flex items-center space-x-1">
      {[...Array(totalFull)].map((_, i) => (
        <Star key={`full-${i}`} className="w-4 h-4 fill-amber-400 text-amber-400" />
      ))}
      {hasHalfStar && <StarHalf className="w-4 h-4 fill-amber-400 text-amber-400" />}
      {[...Array(emptyStars > 0 ? emptyStars : 0)].map((_, i) => (
        <Star key={`empty-${i}`} className="w-4 h-4 text-gray-400" />
      ))}
      <span className="ml-2 text-sm text-gray-300 font-medium">{rating.toFixed(1)}</span>
    </div>
  );
}
