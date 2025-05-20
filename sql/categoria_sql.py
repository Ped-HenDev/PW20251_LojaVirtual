CREATE_TABLE_CATEGORIA = '''
CREATE TABLE IF NOT EXISTS categoria (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL);
'''

INSERT_CATEGORIA = '''
INSERT INTO categoria (nome)
VALUES (?);
'''

UPDATE_CATEGORIA = '''
UPDATE categoria
SET nome = ?
WHERE id = ?;
'''

DELETE_CATEGORIA = '''
DELETE FROM categoria
WHERE id = ?;
'''
GET_CATEGORIA_BY_ID = '''
SELECT id, nome
FROM categoria
WHERE id = ?;
'''

GET_CATEGORIAS_BY_PAGE = '''
SELECT id, nome
FROM categoria
ORDER BY nome ASC
LIMIT ? OFFSET ?;
'''

