<?php

namespace app\index\controller;

use think\Controller;
use think\Request;
use app\common\controller\Common;

class Index extends Base
{
	public function getTopMenu(){
		header('Access-Control-Allow-Origin: *');
        header('Access-Control-Allow-Methods: POST');
        header("Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept");
		$indexModel=model('Index');
		$data=$indexModel->getDataList('');
		return $data;
		
	}

}