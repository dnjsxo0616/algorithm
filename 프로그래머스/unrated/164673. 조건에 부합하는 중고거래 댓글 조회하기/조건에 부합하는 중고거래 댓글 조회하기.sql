-- 코드를 입력하세요
SELECT b.title, b.board_id, r.reply_id, r.writer_id, r.contents, DATE_FORMAT(r.created_date,'%Y-%m-%d') AS created_date
FROM used_goods_board AS b 
JOIN used_goods_reply AS r ON b.board_id = r.board_id
WHERE b.created_date LIKE "2022-10%"
ORDER BY created_date, b.title