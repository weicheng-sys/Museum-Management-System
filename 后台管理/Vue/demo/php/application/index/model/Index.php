<?php
// +----------------------------------------------------------------------
// | Description: 公共模型,所有模型都可继承此模型，基于RESTFUL CRUD操作
// +----------------------------------------------------------------------
// | Author: linchuangbin <linchuangbin@honraytech.com>
// +----------------------------------------------------------------------

namespace app\index\model;

use think\Model;

class Index extends Model 
{
	protected $_IndexMenue="index_menu";

	public function getDataList($keywords)
	{
		$map = [];
		if ($param['keywords']) {
			$map['name'] = ['like', '%'.$keywords.'%'];
		}
		$data = $this->table('oa_index_menu')->where($map)->select();
		return $data;
	}
}