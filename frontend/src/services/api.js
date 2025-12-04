// services/api.js
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

class ApiService {
  async request(endpoint, options = {}) {
    const url = `${API_BASE_URL}${endpoint}`;
    const config = {
      headers: {
        'Content-Type': 'application/json',
        ...options.headers,
      },
      ...options,
    };

    try {
      const response = await fetch(url, config);
      
      if (!response.ok) {
        const error = await response.json().catch(() => ({ detail: response.statusText }));
        throw new Error(error.detail || `HTTP error! status: ${response.status}`);
      }
      
      return await response.json();
    } catch (error) {
      console.error('API request failed:', error);
      throw error;
    }
  }

  async getPersonas() {
    return this.request('/personas');
  }

  async getPersona(personaId) {
    return this.request(`/personas/${personaId}`);
  }

  async startBattle(battleData) {
    return this.request('/battle', {
      method: 'POST',
      body: JSON.stringify(battleData),
    });
  }

  async healthCheck() {
    return this.request('/health');
  }
}

export default new ApiService();

