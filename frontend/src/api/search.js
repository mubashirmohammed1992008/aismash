import axios from 'axios';

const api = axios.create({
    baseURL: 'https://aismash.onrender.com',
});

export const searchProducts = async (query) => {
    try {
        const response = await api.get('/search', {
            params: { product: query }
        });
        return response.data;
    } catch (error) {
        console.error('Error fetching search results:', error);
        throw error;
    }
};

export const analyzeUrl = async (url) => {
    try {
        const response = await api.get('/analyze', {
            params: { url: url }
        });
        return response.data;
    } catch (error) {
        console.error('Error analyzing URL:', error);
        throw error;
    }
};
