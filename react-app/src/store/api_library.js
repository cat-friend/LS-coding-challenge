export async function fetchAllLoans(options = {}) {
    options.method = 'GET';
    const url = `/api/loans/`
    const res = await window.fetch(url, options);
    if (res.status >= 400) throw res;
    return res;
}


export async function fetchOneLoan(id) {
    options.method = 'GET';
    const url = `/api/loans/${id}`
    const res = await window.fetch(url, options);
    if (res.status >= 400) throw res;
    return res;
}

export async function editLoan(payload, options = {}) {
    options.method = 'PUT';
    options.headers = {};
    options.body = JSON.stringify(payload);
    options.headers['Content-Type'] = 'application/json';
    const url = `/api/loans/${payload.id}`
    const res = await window.fetch(url, options);
    if (res.status >= 400) throw res;
    return res;
}

export async function postLoan(payload) {
    options.method = 'POST';
    options.headers = {};
    options.body = JSON.stringify(payload);
    options.headers['Content-Type'] = 'application/json';
    const url = `/api/loans/`
    const res = await window.fetch(url, options);
    if (res.status >= 400) throw res;
    return res;
}
