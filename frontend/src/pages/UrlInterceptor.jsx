import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

export default function UrlInterceptor() {
    const navigate = useNavigate();

    useEffect(() => {
        const path = window.location.pathname; // e.g. /https:/www.amazon.in/...

        const httpsMatch = path.match(/^\/https:\/(.*)/);
        const httpMatch = path.match(/^\/http:\/(.*)/);

        const match = httpsMatch || httpMatch;
        const protocol = httpsMatch ? 'https' : 'http';

        if (match) {
            const rest = match[1]; // e.g. www.amazon.in/product/dp/B09Z7YGV3R
            const externalSearch = window.location.search;
            const fullUrl = `${protocol}://${rest}${externalSearch}`;
            navigate(`/analyze?url=${encodeURIComponent(fullUrl)}`, { replace: true });
        } else {
            // Not a URL path — go home
            navigate('/', { replace: true });
        }
    }, [navigate]);

    return null;
}