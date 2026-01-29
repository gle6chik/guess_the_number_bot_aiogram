const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8080';

export async function getUsers() {
    try {
        const response = await fetch(`${API_URL}/users`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
            cache: 'no-store'
        });

        if (!response.ok) {
            throw new Error(`API error: ${response.status}`);
        }

        return await response.json()
    } catch (error) {
        console.error('Error fetching users:', error);
        throw error;
    }
}

export async function getUsersForChart() {
    try {
        const response = await fetch(`${API_URL}/total_users`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
            cache: 'no-store'
        });

        if (!response.ok) {
            throw new Error(`API error: ${response.status}`);
        }

        return await response.json()
    } catch (error) {
        console.error('Error fetching users for chart:', error);
        throw error;
    }
}
