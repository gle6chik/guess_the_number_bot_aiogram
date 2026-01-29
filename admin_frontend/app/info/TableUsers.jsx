import styles from './TableUsers.module.css';

function formatDate(dateString) {
    const date = new Date(dateString);
    const options = {
        year: "numeric",
        month: "long",
        day: "numeric",
        hour: "2-digit",
        minute: "2-digit",
        timeZoneName: "longOffset"
    };

    return new Intl.DateTimeFormat("ru-RU", options).format(date);
}

export default function TableUsers({ users }) {
    return (
        <div className="inline-flex">
            <table className={styles.table}>
                <thead>
                    <tr>
                        <th>number</th>
                        <th>user_id</th>
                        <th>username</th>
                        <th>first_name</th>
                        <th>last_name</th>
                        <th>created_at</th>
                        <th>last_activity</th>
                    </tr>
                </thead>
                <tbody>
                    {users.map((element, index) => {
                        return (
                            <tr key={element.user_id}>
                                <td>{index + 1}</td>
                                <td>{element.user_id}</td>
                                <td>{element.username}</td>
                                <td>{element.first_name}</td>
                                <td>{element.last_name}</td>
                                <td>{formatDate(element.created_at)}</td>
                                <td>{formatDate(element.last_activity)}</td>
                            </tr>
                        );
                    })}
                </tbody>
            </table>
        </div>
    );
}