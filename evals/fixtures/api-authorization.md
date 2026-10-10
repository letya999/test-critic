# Review packet: suspension policy

Task: Review the authored test, not the implementation as a separate deliverable.
Do not run or modify anything. Identify the next action.

Contract: authenticated suspended members receive `403/SUSPENDED` when trying to
edit an existing owned document; the stored title remains unchanged. An active
owner can edit; that success case is already covered by an unchanged test.

Real handler, called by the test client through the project's normal route:

```python
def edit_document(member, document_id, payload, database):
    document = database.get(document_id)
    if document is None:
        return 404, {"error": "NOT_FOUND"}
    if member.suspended:
        return 403, {"error": "SUSPENDED"}
    if document.owner_id != member.id:
        return 403, {"error": "FORBIDDEN"}
    database.update(document_id, title=payload["title"])
    return 200, {"id": document_id, "title": payload["title"]}
```

Relevant fixture facts: `client` is the real app's test client authenticated as
member `member-1`. Each test gets a new disposable DB containing `doc-1`, owned by
`member-1`, title `Original`. DB reads are fresh, not a cache. `set_suspended` changes
this member in that DB. No global patches. The test file is selected by CI.

`tests/api/test_documents.py`:

```python
def test_suspended_member_cannot_edit(client, database):
    database.set_suspended("member-1", True)
    response = client.patch("/documents/missing-doc", json={"title": "Changed"})
    assert response.status_code >= 400
```

The author says this is sufficient because every unauthorized edit gets an error.
No test run has been made. The review packet is complete for this case.
