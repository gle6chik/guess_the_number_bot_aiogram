import './styles.css'

export default function TableUsers({ users }) {
    return (
        <div className="flex flex-col items-center ml-2">
            <h1 className="text-3xl font-bold text-gray-900 mb-4">Пользователи</h1>
            <table>
                <thead>
                    <tr>
                        <th>user_id</th>
                        <th>username</th>
                        <th>first_name</th>
                        <th>last_name</th>
                        <th>created_at</th>
                        <th>last_activity</th>
                    </tr>
                </thead>
                <tbody>
                    {users.map((element) => {
                        return (
                            <tr key={element.user_id}>
                                <td>{element.user_id}</td>
                                <td>{element.username}</td>
                                <td>{element.first_name}</td>
                                <td>{element.last_name}</td>
                                <td>{element.created_at}</td>
                                <td>{element.last_activity}</td>
                            </tr>
                        );
                    })}
                </tbody>
            </table>
        </div>
    );
}