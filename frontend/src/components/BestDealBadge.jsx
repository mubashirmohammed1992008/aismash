import { ExternalLink, Zap, Tag, CreditCard } from 'lucide-react';
import StarRating from './StarRating';

export default function BestDealBadge({ product }) {
  if (!product) return null;
  const { title, site, price, currency, rating, review_count, url, image_url, original_price, discount_percentage, offers } = product;

  return (
    <div className="glass-card rounded-2xl p-1 shadow-[0_0_15px_rgba(16,185,129,0.3)] bg-gradient-to-br from-emerald/40 to-transparent relative overflow-hidden group">
      <div className="absolute top-0 right-0 bg-emerald text-white font-bold text-sm px-4 py-1.5 rounded-bl-xl shadow-lg flex items-center z-10">
        <Zap className="w-4 h-4 mr-1 pb-0.5 fill-white" /> Best Deal
      </div>
      
      <div className="bg-slate-900 rounded-xl p-6 h-full flex flex-col md:flex-row gap-6 relative z-0">
        <div className="w-full md:w-1/3 h-48 md:h-auto bg-white/5 rounded-lg flex items-center justify-center p-4">
           {image_url ? (
            <img src={image_url} alt={title} className="max-h-full max-w-full object-contain filter drop-shadow-lg" />
          ) : (
            <div className="text-gray-500">Image Preview</div>
          )}
        </div>
        
        <div className="w-full md:w-2/3 flex flex-col justify-center">
          <div className="uppercase tracking-wider text-emerald-400 font-semibold text-xs mb-2">Editor's Choice</div>
          <h2 className="text-2xl md:text-3xl font-bold text-white mb-3 line-clamp-2">
            {title}
          </h2>
          
          <div className="flex items-center space-x-6 mb-4">
            <div className="flex flex-col">
              <span className="text-gray-400 text-sm mb-1">Price</span>
              <div className="flex items-end space-x-2">
                <span className="text-3xl font-bold font-mono text-white">
                  {currency === 'INR' ? '₹' : '$'}{price.toLocaleString()}
                </span>
                {original_price && original_price > price && (
                  <span className="text-sm text-gray-500 line-through mb-1">
                    {currency === 'INR' ? '₹' : '$'}{original_price.toLocaleString()}
                  </span>
                )}
                {discount_percentage > 0 && (
                  <span className="text-sm text-emerald-400 font-bold mb-1">
                    {discount_percentage}% OFF
                  </span>
                )}
              </div>
            </div>
            <div className="w-px h-12 bg-white/10"></div>
            <div className="flex flex-col">
              <span className="text-gray-400 text-sm mb-1">Rating</span>
              <div className="flex items-center">
                <StarRating rating={rating} />
                <span className="ml-2 text-xs text-gray-500">({review_count})</span>
              </div>
            </div>
          </div>
          
          {offers && offers.length > 0 && (
            <div className="mb-6 bg-slate-950/50 rounded-xl p-4 border border-white/5">
              <div className="text-xs font-bold text-gray-400 uppercase tracking-wider mb-2.5 flex items-center">
                 <Tag className="w-4 h-4 mr-2 text-emerald-400" /> Available Bank Offers
              </div>
              <ul className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                 {offers.slice(0, 4).map((offer, idx) => (
                    <li key={idx} className="text-xs text-gray-300 flex items-start bg-white/5 p-2 rounded-lg border border-white/5">
                       <CreditCard className="w-4 h-4 mr-2 text-blue-400 shrink-0" />
                       <span className="leading-snug">{offer}</span>
                    </li>
                 ))}
              </ul>
            </div>
          )}
          
          <div className="mt-auto flex items-center justify-between">
            <span className="text-gray-300 font-medium bg-white/10 px-3 py-1 rounded-full capitalize border border-white/5">
              Found on {site}
            </span>
            <a 
              href={url}
              target="_blank"
              rel="noreferrer"
              className="px-6 py-3 bg-emerald hover:bg-emerald-600 text-white font-bold rounded-xl transition-all duration-300 flex items-center shadow-lg hover:shadow-emerald/50 hover:scale-105"
            >
              Buy Now <ExternalLink className="w-5 h-5 ml-2" />
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}
